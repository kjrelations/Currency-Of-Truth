import sys
import markdown


def create_blog_post(markdown_content):
    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, output_format='html5')
    print(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python markdown_to_html_renderer.py <file_path>")
        sys.exit(1)

    # Get the file path from the command-line argument
    file_path = sys.argv[1]

    try:
        # Open the file for reading
        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the file contents
            content = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    create_blog_post(content)
