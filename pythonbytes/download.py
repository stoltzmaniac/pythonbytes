import requests


# TODO: Everything... it's late right now.
def download_episode(episode_number: int):
    """
    Downloads the podcast file
    :param episode_number:
    :return:
    """
    res = requests.get(f'https://pythonbytes.fm/episodes/download/{episode_number}.mp3')
    with open(f"{episode_number}.mp3", 'wb') as f:
        f.write(res.content)

