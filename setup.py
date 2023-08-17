from setuptools import setup

# Read the contents of README.md
with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='ngboost',
    version='0.1',
    scripts=['ngboost'],
    long_description=long_description,
    long_description_content_type='text/markdown'  # Specify that it's Markdown content
)
