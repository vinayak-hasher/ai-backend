```
def test_view_assigned_pod_and_recommend_colleagues():
    # Setup
    user = UserFactory.create()
    pod = PodFactory.create(assigned_to=user)
    colleague1 = UserFactory.create()
    colleague2 = UserFactory.create()

    # Test viewing assigned pod
    response = client.get(f'/pods/{pod.id}')
    assert response.status_code == 200
    assert response.json()['id'] == pod.id

    # Test recommending colleagues
    response = client.post(f'/pods/{pod.id}/recommend', json={'user_ids': [colleague1.id, colleague2.id]})
    assert response.status_code == 200
    assert response.json()['recommended_colleagues'] == [colleague1.id, colleague2.id]

    # Edge case: user not assigned to pod
    pod.assigned_to = None
    pod.save()
    response = client.get(f'/pods/{pod.id}')
    assert response.status_code == 403

    # Edge case: invalid pod id
    response = client.get('/pods/99999')
    assert response.status_code == 404

    # Edge case: invalid user ids
    response = client.post(f'/pods/{pod.id}/recommend', json={'user_ids': ['invalid', 123]})
    assert response.status_code == 400
```