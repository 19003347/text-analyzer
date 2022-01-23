import string

file = open("filefolder/loki.txt",'w')
file.write("""
Thor's adoptive brother and nemesis, based on the Norse mythological deity of the same name.[25] About his character's evolution from the film Thor, Hiddleston said, "I think the Loki we see in The Avengers is further advanced. You have to ask yourself the question: How pleasant an experience is it disappearing into a wormhole that has been created by some kind of super nuclear explosion of his own making? So I think by the time Loki shows up in The Avengers, he's seen a few things."[33] About Loki's motivations, Hiddleston said, "At the beginning of The Avengers, he comes to Earth to subjugate it and his idea is to rule the human race as their king. And like all the delusional autocrats of human history, he thinks this is a great idea because if everyone is busy worshipping him, there will be no wars so he will create some kind of world peace by ruling them as a tyrant. But he is also kind of deluded in the fact that he thinks unlimited power will give him self-respect, so I haven't let go of the fact that he is still motivated by this terrible jealousy and kind of spiritual desolation
""")


def counter(word,char):
    count=0
    for i in word:
        if char==i:
            count+=1
    return count


file=input("Enter your filename: ")
with open(file) as f:
    text=f.read()

letters=string.ascii_lowercase
for i in letters:
    c=counter(text,i)
    percentage=(c/len(text))*100
    print(f"{i} - {percentage}%")
