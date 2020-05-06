#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - that checks if a singly linked list is a palindrome.
 * @head: linked list
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *end;
	unsigned int n_nodes = 0, i = 0, index = 0;

	if (*head == NULL || head == NULL)
		return (0);

	current = *head;

	while (current != NULL)
	{
		n_nodes += 1;
		current = current->next;
	}

	if (n_nodes % 2 != 0)
		return (0);

	current = *head;
    index = 0;
	for (i = 0; i < n_nodes / 2; i++)
	{
		index = i; 
        end = current;
		while (index != (n_nodes - 1) - i)
		{
			end = end->next;
			index += 1;
		}
		if (current->n != end->n)
			return  (0);
        current = current->next;
	}

	return (1);
}
