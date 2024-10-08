import click
import os


@click.command()
@click.option("--file",prompt=True,prompt_required=False,default="",help="specifies that the path that is being pointed to is a file.")
@click.option("--folder",prompt=True,prompt_required=False,default="",help="specifies that the path that is being pointed to is a folder.")
@click.option("--writefile",prompt=True,prompt_required=False,default="",help="specifies where the metrics Moji recorded should go.")
def read(file,folder,write):
    nline = 0
    if file == "":
        dir = os.listdir(folder)
        for item in dir:
            pass
    if folder == "":
        with open(file,"r") as readfile:  
            for line in readfile:
                n += 1
    else:
        raise click.BadOptionUsage("--file,--folder",message="You did not provide any location to check the metrics of.")
    
    if write is not None:
        click.echo
        ...
