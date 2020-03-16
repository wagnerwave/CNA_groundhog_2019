##
## EPITECH PROJECT, 2020
## Alexandre Wagner - Victor rouxel
## File description:
## Makefile for groundhog project
##

D_SRC	=	./src/

NAME	=	groundhog

$(NAME)	:
			cp $(D_SRC)main.py ./
			mv main.py groundhog
			chmod +x groundhog

all	:	$(NAME)

clean:
		rm -rf groundhog

fclean:	clean

re	:	fclean all

.PHONY: all clean fclean re