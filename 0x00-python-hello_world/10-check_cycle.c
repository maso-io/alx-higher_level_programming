#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tmp;

	if (!list)
		return (0);
	head = list;
	tmp = list->next;
	while (tmp != NULL)
	{
		if (tmp == head)
			return (1);
		tmp = tmp->next;
	}

	return (0);
}
