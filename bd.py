zero=[ "x",
	"x", "x",
	"x", "x",
	   "x"]

jeden=[ "x",
	"x","x",
	    "x",
	  "xxx",]


dwa=["xxxx",
     "x""x",
		"x",
    "x","x"]

trzy=["xxxxx",
	     "x",
	   "xxx",
	     "x",
	  "xxxx",]

cztery=["xx",
      "x","x",		
     "x", "x",
	      "x",
	      "x",]

pięć=["xxxxx",
      "x",
      "x","x",
          "x",	
       "xxxx"]

sześć=["xxx",
	  "x",
	  "x","x"
	  "x","x",
	    "x",]
siedem=["xxxxx",
		   "x",
		  "x",
		  "x"]

osiem=["xxxx",
	  "x", "x",
	  	"x",
	  "x", "x",
	   "xxxx",]

dziwięć=["xxxx",
		"x", "x",
		"x","x",
			"x",
		"x","x",]
			
pass
j=len("a")
a=int(input("podaj liczbe"))
for i in range(5):
	tekst_do_wypisania=""
	for i in range(len("a")):
		if a[j]== '0':
			tekst_do_wypisania+=zero[i]
		if a[j]== '1':
			tekst_do_wypisania+=jeden[i]
		if a[j]== '2':
			tekst_do_wypisania+=dwa[i]
		if a[j]== '3':
			tekst_do_wypisania+=trzy[i]
		if a[j]== '4':
			tekst_do_wypisania+=cztery[i]
		if a[j]== '5':
			tekst_do_wypisania+=pięć[i]
		if a[j]== '6':
			tekst_do_wypisania+=cześć[i]
		if a[j]== '7':
			tekst_do_wypisania+=siedem[i]
		if a[j]== '8':
			tekst_do_wypisania+=osiem[i]
		if a[j]== '9':
			tekst_do_wypisania+=dziewięć[i]
		print(tekst_do_wypisania)
		