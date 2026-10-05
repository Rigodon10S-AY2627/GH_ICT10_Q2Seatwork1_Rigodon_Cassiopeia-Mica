from pyscript import display
from pyscript import document

countries = ['Brunei', 'Cambodia', 'Indonesia', 'Laos', 'Malaysia', 'Myanmar (Burma)', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste (East Timor)', 'Vietnam']

nicknames = ['Land of Unexpected Treasures', 'Kingdom of Wonder', 'Emerald of the Equator', 'Land of a Million Elephants', 'Land of Indigenous Malay', 'Golden Land', 'Pearl of the Orient Seas', 'The Lion City', 'Land of Smiles', 'Land of the Sleeping Crocodile', 'Land of the Blue Dragon']

def show_nickname(e):
    document.querySelector('#result').innerHTML = ''

    index = int(document.querySelector('#country').value)

    display(countries[index], target='result')
    display(nicknames[index], target='result')