
import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the indices
gallery_end_index = -1
schedule_start_index = -1

for i, line in enumerate(lines):
    if '<section id="gallery"' in line:
        # Find the end of gallery section (it ends before the garbage)
        # We know the garbage is before schedule
        pass
    if '<section id="schedule"' in line:
        schedule_start_index = i
        break

# We know the garbage is immediately before schedule_start_index
# Let's look at the lines before schedule
# Expecting:
# ...
# </section> (gallery end)
# </div> (garbage)
# </section> (garbage)
# <section id="schedule"...

# Let's verify
print(f"Line at schedule_start_index ({schedule_start_index}): {lines[schedule_start_index]}")
print(f"Line before: {lines[schedule_start_index-1]}")
print(f"Line before that: {lines[schedule_start_index-2]}")
print(f"Line before that: {lines[schedule_start_index-3]}")

# We want to replace the garbage lines with the Videos section
# The Videos section HTML
videos_section = """
        <section id="videos" class="py-16 bg-white">
            <div class="container mx-auto px-6 text-center">
                <h2 class="section-title text-3xl font-bold mb-12 text-red-600">Highlight Videos</h2>
                <p class="text-lg mb-8">Watch highlights and game footage.</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
                    <div class="aspect-w-16 aspect-h-9">
                        <iframe class="w-full h-64 rounded-lg shadow-lg" src="https://www.youtube.com/embed/placeholder1" title="Highlight Video 1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                    <div class="aspect-w-16 aspect-h-9">
                        <iframe class="w-full h-64 rounded-lg shadow-lg" src="https://www.youtube.com/embed/placeholder2" title="Highlight Video 2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    </div>
                </div>
                <div class="mt-12">
                    <a href="#" class="btn-secondary font-bold py-3 px-8 rounded-lg text-lg uppercase shadow-md hover:shadow-xl transform hover:scale-105 transition-transform duration-300">View More on YouTube</a>
                </div>
            </div>
        </section>
"""

# Check if lines before schedule are indeed the garbage
if '</div>' in lines[schedule_start_index-2] and '</section>' in lines[schedule_start_index-1]:
    print("Found garbage tags. Removing and inserting Videos section.")
    # Remove the two lines
    del lines[schedule_start_index-1] # Remove </section>
    del lines[schedule_start_index-2] # Remove </div> (index shifted? No, if we delete higher index first)
    
    # Wait, if I delete index-1, then index-2 becomes index-1?
    # Better to slice.
    
    # Re-read to be safe or just use slicing
    # We want lines[:schedule_start_index-2] + videos_section + lines[schedule_start_index:]
    
    new_lines = lines[:schedule_start_index-2] + [videos_section] + lines[schedule_start_index:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("File updated successfully.")
else:
    print("Garbage tags not found exactly where expected. Aborting.")
    # Print context for debugging
    for j in range(max(0, schedule_start_index-5), schedule_start_index+1):
        print(f"{j}: {lines[j].rstrip()}")
