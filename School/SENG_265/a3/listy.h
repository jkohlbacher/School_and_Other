/** @file listy.h
 *  @brief Function prototypes for the linked list.
 */
#ifndef _LINKEDLIST_H_
#define _LINKEDLIST_H_

typedef struct FAT_t {
	uint32_t entry;
} FAT_t;


/**
 * @brief An struct that represents a node in the linked list.
 */
typedef struct node_t
{
    // The val associated with a node in the list.
    FAT_t *val;
    // The next (linked) mode in the list.
    struct node_t *next;

} node_t;

/**
 * Function protypes associated with a linked list.
 */
node_t *new_node(event_t *);
node_t *add_front(node_t *, node_t *);
node_t *add_end(node_t *, node_t *);
node_t *peek_front(node_t *);
node_t *remove_front(node_t *);
void apply(node_t *, void (*fn)(node_t *, void *), void *arg);
void free_list(node_t *);

#endif