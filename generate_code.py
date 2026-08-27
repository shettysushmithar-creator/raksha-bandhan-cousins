import random

names = ['Rathan', 'Mithun', 'Samarth', 'Sukesh', 'Sandarshan', 'Adhu Anna', 'Pavi Anna Makkimane', 'Veera Anna', 'Sura', 'Madhu Anna', 'Manu Anna', 'Vinod Anna', 'Chinna', 'Nanda Anna', 'Pradeep Anna', 'Rithivik', 'Nadmani Pavi Anna', 'Abhi', 'Prasha Anna', 'Ravi Anna', 'Raja Anna', 'Ragu Anna']
tags = ['the amazing brother', 'always there for me', 'partner in crime', 'the cool cousin', 'the protector', 'my secret keeper', 'the fun one', 'the troublemaker', 'always smiling', 'the best advisor']

random.seed(42)
html = []
js = []
for n in names:
    tag = random.choice(tags)
    theme = n.replace(' ', '')
    html.append(f'''        <button class="planet" data-theme="{theme}" data-name="{n}" aria-haspopup="dialog">
          <div class="planet-orb"><div class="initial">{n[0]}</div></div>
          <div class="planet-name">{n}</div>
          <div class="planet-tag">{tag}</div>
        </button>''')
    js.append(f'''      "{n}": {{
        role: "{tag}",
        paragraphs: [
          "Happy Raksha Bandhan! Even though we might not see each other every day, you're always in my thoughts.",
          "Thank you for always being such a wonderful brother and for always looking out for me. You mean so much to our family.",
          "Here is your virtual rakhi! Wishing you all the happiness and success in the world. Love you!"
        ]
      }},''')

with open('scratch.txt', 'w') as f:
    f.write('\n'.join(html))
    f.write('\n===============\n')
    f.write('\n'.join(js))
