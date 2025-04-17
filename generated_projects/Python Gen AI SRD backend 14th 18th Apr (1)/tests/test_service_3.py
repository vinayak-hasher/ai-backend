```
import pytest
from your_app.models import User, Pod

@pytest.fixture
def user():
    return User.objects.create(username='test_user')

@pytest.fixture
def pod():
    return Pod.objects.create(name='test_pod')

def test_user_can_view_assigned_pod(user, pod):
    user.pod = pod
    user.save()
    assert user.pod == pod

def test_user_cannot_view_unassigned_pod(user, pod):
    assert user.pod is None

def test_user_can_recommend_colleagues_for_inclusion(user, pod):
    colleague = User.objects.create(username='test_colleague')
    user.pod = pod
    user.save()
    pod.recommended_colleagues.add(colleague)
    assert colleague in pod.recommended_colleagues.all()

def test_user_cannot_recommend_colleagues_for_unassigned_pod(user, pod):
    colleague = User.objects.create(username='test_colleague')
    with pytest.raises(ValueError):
        pod.recommended_colleagues.add(colleague)
```