#include <stdlib.h>
#include "lists.h"
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *next;
    int is_palin = 1;

    if (*head && (*head)->next) {
        while (fast && fast->next) {
            fast = fast->next->next;
            next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }

        fast = (fast) ? slow->next : slow;

        while (prev && is_palin) {
            is_palin &= (prev->n == fast->n);
            fast = fast->next;
            next = prev->next;
            prev->next = slow;
            slow = prev;
            prev = next;
        }
    }

    return is_palin;
}