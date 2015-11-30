def joint(text):
      replaced = ''
      for i in text:
          if i == ' ':
              replaced = replaced + ''
          else:
              replaced = replaced + i
      return replaced


print(joint('asg asg wigo'))
