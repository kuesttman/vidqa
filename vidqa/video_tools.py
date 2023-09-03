from __future__ import annotations

import logging
import os
import re


def convert_only_audio(
    path_file_video_origin: str, path_file_video_dest: str
) -> None:

    """Make release for mp4 H264/AAC reencoding only audio

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
    """

    logging.info(
        "Convert video extension without reencode: %s", path_file_video_origin
    )
    # Obtenha o nome do arquivo de origem sem a extensão
    nome_arquivo_origem = os.path.splitext(os.path.basename(path_file_video_origin))[0]

    # Separar o nome do arquivo da extensão
    nome_base, extensao = os.path.splitext(nome_arquivo_origem)

    # Remover conteúdo entre colchetes usando expressão regular
    padrao = r'\[.*?\]'
    nome_limpo = re.sub(padrao, '', nome_base).strip()

    # Adicionar "By: @Sk4rFx" ao título limpo
    novo_titulo = f"{nome_limpo} -> By: @Sk4rFx <-"

    stringa = (
        f'ffmpeg -v quiet -stats -y -i "{path_file_video_origin}" '
        + "-vcodec copy "
        + "-map 0 "
        + "-map a "
        + "-map s "
        + "-c:s srt "
        + f'-metadata title="{novo_titulo}" '
        + f'-c:a aac "{path_file_video_dest}"'
    )
    print("\n", stringa)
    os.system(stringa)
    logging.info("Done")


def convert_mp4_wo_reencode(
    path_file_video_origin: str, path_file_video_dest: str
) -> None:
    """Make release for mp4 H264/AAC without reencode

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
    """

    logging.info(
        "Convert video extension without reencode: %s", path_file_video_origin
    )
    # Obtenha o nome do arquivo de origem sem a extensão
    nome_arquivo_origem = os.path.splitext(os.path.basename(path_file_video_origin))[0]

    # Separar o nome do arquivo da extensão
    nome_base, extensao = os.path.splitext(nome_arquivo_origem)

    # Remover conteúdo entre colchetes usando expressão regular
    padrao = r'\[.*?\]'
    nome_limpo = re.sub(padrao, '', nome_base).strip()

    # Adicionar "By: @Sk4rFx" ao título limpo
    novo_titulo = f"{nome_limpo} -> By: @Sk4rFx <-"

    stringa = (
        f'ffmpeg -v quiet -stats -y -i "{path_file_video_origin}" '
        + "-map 0 "
        + "-map a "
        + "-map s "
        + "-c:s srt "
        + "-c:v copy "
        + "-c:a copy "
        + f'-metadata title="{novo_titulo}" '
        + f'"{path_file_video_dest}"'
    )
    print("\n", stringa)
    os.system(stringa)
    logging.info("Done")


def convert_mp4_aac_get_stringa(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> str:
    """get ffmpeg command to reencode a video as mp4 H264/AAC

    Args:
        path_file_video_origin (str): input video path
        path_file_video_dest (str): output video path
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.

    Returns:
        str: ffmpeg string command
    """
    # Obtenha o nome do arquivo de origem sem a extensão
    nome_arquivo_origem = os.path.splitext(os.path.basename(path_file_video_origin))[0]

    # Separar o nome do arquivo da extensão
    nome_base, extensao = os.path.splitext(nome_arquivo_origem)

    # Remover conteúdo entre colchetes usando expressão regular
    padrao = r'\[.*?\]'
    nome_limpo = re.sub(padrao, '', nome_base).strip()

    # Adicionar "By: @Sk4rFx" ao título limpo
    novo_titulo = f"{nome_limpo} -> By: @Sk4rFx <-"

    crf = float(flags.get("crf", 18))
    maxrate = float(flags.get("maxrate", 4))
    bufsize = maxrate * 2
    stringa = (
        f"ffmpeg -v quiet -stats -y "
        + f'-i "{path_file_video_origin}" '
        + "-c:v h264_nvenc "
        + f"-crf {str(crf)} "
        + f"-maxrate {str(maxrate)}M "
        + f"-bufsize {str(bufsize)}M "
        + "-preset medium "
        + "-flags +global_header "
        + "-vf format=yuv420p "
        + "-profile:v main "
        + "-movflags +faststart "
        + "-map 0 "
        + "-c:a aac "
        + "-map a "
        + "-map s "
        + "-c:s srt "
        + f'-metadata title="{novo_titulo}" '
        + f'"{path_file_video_dest}"'
    )
    return stringa


def convert_mp4_aac(
    path_file_video_origin: str,
    path_file_video_dest: str,
    flags: dict = {"crf": 18, "maxrate": 4},
) -> None:
    """Make release for mp4 H264/AAC

    Args:
        path_file_video_origin (str): Original video file path
        path_file_video_dest (str): Path of the edited video file
        flags (dict, optional): video conversion flags.
            Defaults to {'crf': 18, 'maxrate': 4}.
    """

    stringa = convert_mp4_aac_get_stringa(
        path_file_video_origin, path_file_video_dest, flags
    )
    print("\n", stringa)
    os.system(stringa)
    logging.info("Done")
