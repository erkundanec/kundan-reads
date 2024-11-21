import subprocess
import os

def build_sphinx_html(source_dir, build_dir):
    try:
        with open(os.devnull, 'w') as null:
            # Running the Sphinx build without a timeout
            result = subprocess.run(
                ["sphinx-build", "-b", "html", source_dir, build_dir], 
                check=True, 
                stderr=null, 
                timeout=None  # No timeout to allow the build process to complete without interruption
            )
        print("Sphinx build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Sphinx build failed with error code {e.returncode}")
    except KeyboardInterrupt:
        print("Build process was interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    source_directory = "./source"  # Make sure this path is correct
    build_directory = "./builddir"  # Make sure this path is correct
    build_sphinx_html(source_directory, build_directory)
