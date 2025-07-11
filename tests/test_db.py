from dataclasses import asdict

from sqlalchemy import select

from fastapi_zeroo.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='test',
            password='secret',
            email='test@example.com',
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'test@example.com',
        'create_at': time,
        'updated_at': time,
    }
