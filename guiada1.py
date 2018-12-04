# -*- coding: utf-8 -*-
# Santiago Bermúdez y John Torres declaramos que esta solución
# es fruto exclusivamente de nuestro trabajo personal. No hemos sido
# ayudados por ninguna otra persona ni hemos obtenido la solución de
# fuentes externas, y tampoco hemos compartido nuestra solución con
# nadie. Declaramos además que no hemos realizado de manera desho-
# nesta ninguna otra actividad que pueda mejorar nuestros resultados
# ni perjudicar los resultados de los demás.

import requests
import xml.etree.ElementTree as ET

# Titulo (cadena de texto) de todos los libros de informatica (genero Computer).
def books_by_genre(genre):
    q = """ for $e in doc("/db/sgdi/books.xml")/catalog/book let $t := $e/title
    where $e/genre = '""" + genre + """'
    return $t """
    req = { '_query': q }
    r = requests.post('http://localhost:8080/exist/rest/db', data = req)
    print(r.text)

# Titulo (cadena de texto) del libro con identificador "bk105".
def books_by_id(id):
    q = """ for $e in doc("/db/sgdi/books.xml")/catalog/book let $t := $e/title
        where $e/@id = '""" + id + """'
        return $t """
    req = { '_query': q }
    r = requests.post('http://localhost:8080/exist/rest/db', data = req)
    print(r.text)

# Tuplas (titulo, precio) con la informacion de todos los libros. Tambien se permite devolver diccionarios Python en lugar de tuplas.
def books_with_price():
    q = """ for $e in doc("/db/sgdi/books.xml")/catalog/book let $t := $e/title, $p := $e/price
        return ($t, $p) """
    req = { '_query': q }
    r = requests.post('http://localhost:8080/exist/rest/db', data = req)
    print(r.text)

# Nombres (cadena de texto) de los libros que cuestan mas de 15e, ordenados por fecha de publi- cacion ascendente.
def books_price_greater_than(price):
    q = """ for $e in doc("/db/sgdi/books.xml")/catalog/book let $t := $e/title, $p := $e/price
        where $p >= """ + str(price) + """
        order by $t ascending
        return $t"""
    req = { '_query': q }
    r = requests.post('http://localhost:8080/exist/rest/db', data = req)
    print(r.text)

# Tuplas o diccionarios(titulo, autor, precio) de los libros de genero Computer que cuestan mas de 40e.
def books_price_greater_than_genre(price, genre):
    q = """ for $e in doc("/db/sgdi/books.xml")/catalog/book let $t := $e/title, $a := $e/author, $p := $e/price
        where $p >= """ + str(price) + """ and $e/genre = '""" + genre + """'
        return ($t, $p, $a) """
    req = { '_query': q }
    r = requests.post('http://localhost:8080/exist/rest/db', data = req)
    print(r.text)

print('-----------------------------------------------------------------------------------------------------')
print('Titulo (cadena de texto) de todos los libros de informatica (genero Computer).')
print('-----------------------------------------------------------------------------------------------------')
books_by_genre('Computer')
print('-----------------------------------------------------------------------------------------------------')
print('Titulo (cadena de texto) del libro con identificador "bk105".')
print('-----------------------------------------------------------------------------------------------------')
books_by_id('bk105')
print('-----------------------------------------------------------------------------------------------------')
print('Tuplas (titulo, precio) con la informacion de todos los libros. Tambien se permite devolver diccionarios Python en lugar de tuplas.')
print('-----------------------------------------------------------------------------------------------------')
books_with_price()
print('-----------------------------------------------------------------------------------------------------')
print('Nombres (cadena de texto) de los libros que cuestan mas de 15€, ordenados por fecha de publicacion ascendente.')
print('-----------------------------------------------------------------------------------------------------')
books_price_greater_than(15)
print('-----------------------------------------------------------------------------------------------------')
print('Tuplas o diccionarios(titulo, autor, precio) de los libros de genero Computer que cuestan mas de 40e.')
print('-----------------------------------------------------------------------------------------------------')
books_price_greater_than_genre(40, 'Computer')
print('-----------------------------------------------------------------------------------------------------')
