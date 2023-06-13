'''Task 1 - is to set up a Git repository'''

'''Task 2'''

#Just a boring print function
print("this world is to small for both of us\n")
#Print with end parameter
print("can I get a HOOYYYAAAA", end="!?!\n\n")
#print with separator
print(1,2,3,4,5,"\n", sep=" | ")

'''Task 3'''
#Letter 'O'
print("#########","\n#\t#"*3,"\n#########\n")
#letter 'H'
print("\n#\t#\n#\t#\n#########\n#\t#\n#\t#\n")

#Some string templates for practice
git_name = "github.com:your-username"
git_repository = "repository.git"
print(f"Use the following command to set the remote URL: git remote set-url origin git@{git_name}/{git_repository}.\nReplace 'your-username' and 'repository' with your actual GitHub username and the name of your repository.")
output_with_format = "When commiting your changes, don't forget to add: {commit_parameter}.".format(commit_parameter = '-m "Your commit message"')
print(output_with_format)
name = "Alex"
age = 25
food = "icecream and chiken"
price = 50
output_with_sd = "My name is %s and I am %d years old. I like %s and my hoody costs $%d" % (name, age, food, price)
print(output_with_sd)