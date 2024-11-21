import subprocess
# import warnings
import os

def build_sphinx_html(source_dir, build_dir):
    try:
        with open(os.devnull, 'w') as null:
            subprocess.run(["sphinx-build", "-b", "html", source_dir, build_dir], check=True, stderr=null)
        print("Sphinx build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Sphinx build failed with error code {e.returncode}")

if __name__ == "__main__":
    source_directory = "./source"
    build_directory = "builddir"
    build_sphinx_html(source_directory, build_directory)

# import subprocess
# import os

# def build_sphinx_html(source_dir, build_dir):
#     try:
#         result = subprocess.run(
#             ["sphinx-build", "-b", "html", source_dir, build_dir],
#             check=True,
#             text=True,
#             capture_output=True  # Capture stdout and stderr
#         )
#         print("Sphinx build completed successfully!")
#         print(result.stdout)  # Optionally display the output
#     except subprocess.CalledProcessError as e:
#         print(f"Error: Sphinx build failed with error code {e.returncode}")
#         print("Error details:")
#         print(e.stderr)  # Display the error details for debugging

# if __name__ == "__main__":
#     source_directory = "./source"
#     build_directory = "builddir"
#     build_sphinx_html(source_directory, build_directory)

