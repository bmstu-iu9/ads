#ifndef ELEM_H_INCLUDED
#define ELEM_H_INCLUDED

struct Elem {
        /* «Тег», описывающий тип значения в «головe» списка */
        enum {
                INTEGER,
                FLOAT,
                LIST
        } tag;

        /* Само значение в «голове» списка */
        union {
                int i;
                float f;
                struct Elem *list;
        } value;

        /* Указатель на «хвост» списка */
        struct Elem *tail;
};

#endif
/* vim: set sw=0 ts=4 noet: */
