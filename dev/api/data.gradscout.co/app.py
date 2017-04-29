#!/usr/bin/env python
"""Flask App v1."""

from flask import Flask, jsonify, abort, make_response, request, url_for
from database import Firebase

app = Flask(__name__)
firebase = Firebase()


@app.route('/api/programs/<int:program_id>', methods=['GET'])
def get_detailed_program(program_id):
    """Get the Detailed Program Details for a given Program ID."""
    return jsonify(firebase.get_detailed_program(program_id))


@app.route('/api/programs/', methods=['GET'])
def get_all_programs():
    """Get complete data for quicker cached access.

    Returns:
        programs (json): JSON Data of Complete Program Details
    """
    return jsonify(firebase.data)


@app.route('/api/programs/count/', methods=['GET'])
def get_program_count():
    """Get the total count of programs available in the database.

    Returns:
        count (json): Total count of the programs in the database
    """
    return jsonify({"count": firebase.get_program_count()})


@app.route('/api/programs/<int:program_id>/research', methods=['GET'])
def get_program_research(program_id):
    """Get the Program Research Details for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        research (json): Python Dict of Research Details
    """
    return jsonify(firebase.get_program_research(program_id))


@app.route('/api/programs/<int:program_id>/admission_rate', methods=['GET'])
def get_program_admission_rate(program_id):
    """Get the Admission Rate for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        admission_rate (int): Admission Rate in Percentage
    """
    return jsonify(firebase.get_program_admission_rate(program_id))


@app.route('/api/programs/<int:program_id>/fees', methods=['GET'])
def get_program_fees(program_id):
    """Get the Program Fees for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        fees_dict (dict): Python Dict of Program Fees
    """
    return jsonify(firebase.get_program_fees(program_id))


@app.route('/api/programs/<int:program_id>/academic_requirements', methods=['GET'])
def get_program_acad(program_id):
    """Get the Academic Requirements for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        acad_dict (dict): Python Dict of Academic Requirement Details
    """
    return jsonify(firebase.get_program_acad(program_id))


@app.route('/api/programs/<int:program_id>/living_expenditure', methods=['GET'])
def get_program_living(program_id):
    """Get the Living Expenses for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        program_dict (dict): Python Dict of Living Expense Details
    """
    return jsonify(firebase.get_program_living(program_id))


@app.route('/api/programs/<int:program_id>/location', methods=['GET'])
def get_program_location(program_id):
    """Get the Location Details of a given Program ID.

    Returns:
        location_dict (dict): Python Dict of Location Details
    """
    return jsonify(firebase.get_program_location(program_id))


@app.route('/api/programs/<int:program_id>/ownership', methods=['GET'])
def get_program_ownership(program_id):
    """Get the Ownership Details for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        ownership_dict (dict): Python Dict of Ownership Details
    """
    return jsonify(firebase.get_program_ownership(program_id))


@app.route('/api/programs/<int:program_id>/program', methods=['GET'])
def get_program_details(program_id):
    """Get the Program Details for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        program_dict (dict): Python Dict of Program Details
    """
    return jsonify(firebase.get_program_details(program_id))


@app.route('/api/programs/<int:program_id>/university', methods=['GET'])
def get_program_university(program_id):
    """Get the University Details for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        program_dict (dict): Python Dict of University Details
    """
    return jsonify(firebase.get_program_university(program_id))


@app.route('/api/programs/<int:program_id>/rank', methods=['GET'])
def get_program_rank(program_id):
    """Get the Rank Details for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        program_dict (dict): Python Dict of Rank Details
    """
    return jsonify(firebase.get_program_rank(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest', methods=['GET'])
def get_detailed_interests(program_id):
    """Get the Detailed Area of Interests for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        areaofinterest_dict (dict):
        Python Dict of detailed Area of Interest Scores
    """
    return jsonify(firebase.get_detailed_interests(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/business_intelligence', methods=['GET'])
def get_aoi_business_intelligence(program_id):
    """Get the Business Intelligence AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Business Intelligence AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_business_intelligence(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/computer_networks', methods=['GET'])
def get_aoi_computer_networks(program_id):
    """Get the Computer Networks AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Computer Networks AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_computer_networks(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/data_science_analytics', methods=['GET'])
def get_aoi_data_science_analytics(program_id):
    """Get the Data Science Analytics AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Data Science Analytics AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_data_science_analytics(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/distributed_systems', methods=['GET'])
def get_aoi_distributed_systems(program_id):
    """Get the Distributed Systems AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Distributed Systems AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_distributed_systems(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/human_center_design_engineering', methods=['GET'])
def get_aoi_hcde(program_id):
    """Get the HCDE AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): HCDE AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_hcde(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/information_architecture', methods=['GET'])
def get_aoi_information_architecture(program_id):
    """Get the Information Architecture AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Information Architecture AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_information_architecture(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/information_assurance_cyber_security', methods=['GET'])
def get_aoi_security(program_id):
    """Get the Info Assurance & Cyber Security AOI Score for a Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Info Assurance & CyberSecurity AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_security(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/library_science', methods=['GET'])
def get_aoi_library_science(program_id):
    """Get the Library Science AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Library Science AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_library_science(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/management_consulting', methods=['GET'])
def get_aoi_management_consulting(program_id):
    """Get the Management & Consulting AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Management & Consulting AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_management_consulting(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/software_engineering', methods=['GET'])
def get_aoi_software_engineering(program_id):
    """Get the Software Engineering AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Software Engineering AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_software_engineering(program_id))


@app.route('/api/programs/<int:program_id>/areaofinterest/web_application_development', methods=['GET'])
def get_aoi_web_app_development(program_id):
    """Get the Web Application Development AOI Score for a given Program ID.

    Args:
        program_id (int): Unique ID for Program

    Returns:
        score (dict): Web Application Development AOI Score of a Program
    """
    return jsonify(firebase.get_aoi_web_app_development(program_id))


@app.errorhandler(404)
def not_found(error):
    """Overriding the default 404 error."""
    return make_response(jsonify({'error': 'Not found'}), 404)


def make_public_task(task):
    """Creating the URI for each tasks."""
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

if __name__ == '__main__':
    app.run(debug=True)
