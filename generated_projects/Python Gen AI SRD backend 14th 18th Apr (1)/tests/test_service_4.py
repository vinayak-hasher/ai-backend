```
def test_manager_can_access_team_leave_history_reports():
    # Setup
    manager = UserFactory(role='manager')
    team_member = UserFactory(role='team_member')
    team_member.team = manager.team
    leave_report = LeaveReportFactory(team_member=team_member)

    # Test
    response = client.get(f'/reports/team_leave_history/{manager.team.id}/', headers={'Authorization': f'Bearer {manager.token}'})

    # Assertions
    assert response.status_code == 200
    assert len(response.json()['leave_reports']) == 1
    assert response.json()['leave_reports'][0]['team_member_id'] == team_member.id

def test_non_manager_cannot_access_team_leave_history_reports():
    # Setup
    non_manager = UserFactory(role='team_member')
    team_member = UserFactory(role='team_member')
    team_member.team = non_manager.team
    leave_report = LeaveReportFactory(team_member=team_member)

    # Test
    response = client.get(f'/reports/team_leave_history/{non_manager.team.id}/', headers={'Authorization': f'Bearer {non_manager.token}'})

    # Assertions
    assert response.status_code == 403

def test_manager_cannot_access_other_team_leave_history_reports():
    # Setup
    manager = UserFactory(role='manager')
    other_team_member = UserFactory(role='team_member')
    other_team_member.team = TeamFactory()
    leave_report = LeaveReportFactory(team_member=other_team_member)

    # Test
    response = client.get(f'/reports/team_leave_history/{other_team_member.team.id}/', headers={'Authorization': f'Bearer {manager.token}'})

    # Assertions
    assert response.status_code == 403
```