import subprocess

def build_sphinx_html(source_dir, build_dir):
    try:
        subprocess.run(["sphinx-build", "-b", "html", source_dir, build_dir], check=True)
        print("Sphinx build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error: Sphinx build failed with error code {e.returncode}")

if __name__ == "__main__":
    source_directory = "./source"
    build_directory = "builddir"
    build_sphinx_html(source_directory, build_directory)
