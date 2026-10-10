from rich import print

nom = input("Quel est ton nom ? ")

if nom == "Evy":
    print("[green]Accès autorisé[/green]")
else:
    print("[red]Accès refusé[/red]")