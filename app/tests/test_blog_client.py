import unittest
from . import BaseTestClass
from app.models import Post
from app.auth.models import User


class BlogClientTestCase(BaseTestClass):
    def test_index_with_no_posts(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'No hay entradas', res.data)

    # Test para comprobar listado de entradas de la pagina principal
    def test_index_with_posts(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Post de prueba',
                        content='Lorem Ipsum')
            post.save()
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertNotIn(b'No hay entradas', res.data)

    # Test para comprobar la redireccion a la pagina login
    def test_redirect_to_login(self):
        res = self.client.get('/admin/')
        self.assertEqual(302, res.status_code)
        self.assertIn('login', res.location)


"""
    # Test para comprobar acceso no autorizado a usuarios invitados
    def test_unauthorized_access_to_admin(self):
        self.login('guest@xyz.com', '1111')
        res = self.client.get('/admin/')
        self.assertEqual(401, res.status_code)
        self.assertIn(b'Ooops!! No tienes permisos de acceso', res.data)

    # Test para comprobar acceso autorizado a un usuario administrador
    def test_authorized_access_to_admin(self):
        self.login('admin@xyz.com', '1111')
        res = self.client.get('/admin/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'Posts', res.data)
        self.assertIn(b'Usuarios', res.data)
"""

if __name__ == '__main__':
    unittest.main()
