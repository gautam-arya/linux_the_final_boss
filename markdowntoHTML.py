import markdown

def md_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        text = f.read()
    html = markdown.markdown(text)
    with open(output_file, 'w') as f:
        f.write(html)


