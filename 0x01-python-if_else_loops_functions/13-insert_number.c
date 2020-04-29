#include "lists.h"
#include <stdio.h>

/**
 * insert_node - Insert in sorted linked list
 *
 * @head: linked list
 * @number: insert number
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *new;

	if (head == NULL)
		return (NULL);

	tmp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	while (tmp != NULL)
	{
		if (tmp->next->n > number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}

		tmp = tmp->next;
	}
	return (NULL);
}
