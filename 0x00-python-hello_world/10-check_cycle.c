
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - that checks if a singly linked list has a cycle in it
 * @list: the list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1 = NULL;

	if (list == NULL)
		return (0);

	temp1 = list;

	while (list != NULL)
	{
		list = list->next;
		if (temp1 == list)
			return (1);
	}

	return (0);
}
