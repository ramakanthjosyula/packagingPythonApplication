import helloWorld


class TestHelloWorld:

    def test_doHello(self):
        assert '"Hello, World!" program - Wikipedia' == \
               helloWorld.do_hello(helloWorld.URL)
