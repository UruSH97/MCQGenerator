from setuptools import find_packages,setup

setup(
    name='Generatemcqs',
    version='1.0.0',
    author='uroosha rahat',
    author_email='urooshashekh@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
