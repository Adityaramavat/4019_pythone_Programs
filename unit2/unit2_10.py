import zipfile
import os

def create_dummy_files():
    """Creates a few sample text files so we have something to zip."""
    files = ['report.txt', 'data.csv', 'notes.txt']
    for file in files:
        with open(file, 'w') as f:
            f.write(f"This is some sample content for {file}.")
    print("Created sample files: report.txt, data.csv, notes.txt\n")

def zip_specific_files(files_to_zip, zip_filename):
    """Zips a list of specific files into a new archive."""
    print(f"--- ZIPPING FILES INTO '{zip_filename}' ---")
    
    # Open a new zip file in 'w' (write) mode. 
    # ZIP_DEFLATED applies standard zip compression to reduce file size.
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file in files_to_zip:
            if os.path.exists(file):
                zip_file.write(file)
                print(f" Successfully added: {file}")
            else:
                print(f" Warning: '{file}' not found. Skipped.")
                
    print("Zipping complete!\n")

def unzip_all(zip_filename, extract_folder):
    """Unzips all contents of an archive into a specific folder."""
    print(f"--- UNZIPPING '{zip_filename}' ---")
    
    if os.path.exists(zip_filename):
        # Open the zip file in 'r' (read) mode
        with zipfile.ZipFile(zip_filename, 'r') as zip_file:
            # Extract everything into the target folder
            zip_file.extractall(extract_folder)
            print(f" Successfully extracted all files into the '{extract_folder}' folder.")
    else:
        print(f" Error: '{zip_filename}' does not exist.")
        
    print("Unzipping complete!\n")

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Create some dummy files to test with
    create_dummy_files()
    
    # 2. Define which specific files we want to zip up
    files_we_want_to_zip = ['report.txt', 'notes.txt'] 
    archive_name = 'my_archive.zip'
    
    # 3. Zip those specific files
    zip_specific_files(files_we_want_to_zip, archive_name)
    
    # 4. Unzip the newly created archive into a folder called 'Extracted_Files'
    unzip_all(archive_name, 'Extracted_Files')