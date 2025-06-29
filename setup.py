from setuptools import setup

setup(
    name='AZMusicAPI',
    version='1.6.0',
    author='AZ Studio',
    description='轻松访问音乐信息和歌曲音频链接 | Easy access to music information and song audio links',
    long_description=open('readme.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    packages=['AZMusicAPI'],
    install_requires=['requests', 'bilibili-api-python'],
    project_urls={
        'GitHub': 'https://github.com/AZ-Studio-2023/AZMusicAPI/'
    },
)
