"""Console script for user_story_generator."""
import sys
import click


@click.command()
def main(args=None) -> int:
    """Console script for user_story_generator."""
    click.echo("Replace this message by putting your code into "
               "user_story_generator.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
