import datetime
import typing


class Message(typing.NamedTuple):
    title : str
    source : typing.Optional[str]
    datetime : typing.Optional[str]
    text : typing.Optional[str]

    def prepare_markdown(self) -> typing.List[typing.Tuple]:
        return [
            ('Title', self.title),
            ('Source', self.source),
            ('Date', self.datetime),
            ('Text', self.text)
        ]

    @staticmethod
    def make_alert(text):
        return Message(
            title='Alert',
            source='@PersonalSenderBot',
            datetime=datetime.datetime.now(),
            text='error: {}'.format(text),
        )


class Event(typing.NamedTuple):
    methods: typing.List[str]
    message: Message
