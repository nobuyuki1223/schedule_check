from skpy import Skype
sk = Skype("test202003302020@outlook.jp", "higurashi3221")

c = sk.contacts["live:.cid.a26d698235676e43"].chat

c.sendMsg("ハロー")
