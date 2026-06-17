import pytest
from unittest.mock import patch, mock_open
from school import find_record, add_student, del_student

# ── Shared sample data ─────────────────────────────────────────────────────────
SAMPLE = {
    "sean@email.com": [
        "sean@email.com", "Sean Dombe", "01-01-2005", "Male",
        "Zimbabwean", "263771234567", "Harare", "John Dombe",
        "263771234568", "Alheit High", "Form 4", "06/17/2025 10:00 AM"
    ]
}


# ══════════════════════════════════════════════════════════════════════════════
# find_record
# ══════════════════════════════════════════════════════════════════════════════

def test_find_record_found(capsys):
    """Returns True and prints record when email exists."""
    with patch("builtins.input", return_value="sean@email.com"):
        result = find_record(SAMPLE)

    assert result is True
    captured = capsys.readouterr()
    assert "Sean Dombe" in captured.out


def test_find_record_not_found(capsys):
    """Returns False and prints error when email is missing."""
    with patch("builtins.input", return_value="ghost@email.com"):
        result = find_record(SAMPLE)

    assert result is False
    captured = capsys.readouterr()
    assert "not found" in captured.out.lower()


# ══════════════════════════════════════════════════════════════════════════════
# add_student
# ══════════════════════════════════════════════════════════════════════════════

def test_add_student_writes_to_file(tmp_path):
    """Student data gets written to the CSV file."""
    csv_file = tmp_path / "records.csv"
    # Write header so the file exists
    csv_file.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")

    inputs = [
        "new@email.com",   # email (from valid_email)
        "Jane Doe",        # name
        "02-02-2004",      # dob
        "Female",          # gender
        "Zimbabwean",      # nationality
        "263770000000",    # phone
        "Bulawayo",        # address
        "Mary Doe",        # emergency contact
        "263770000001",    # emergency phone
        "Test High",       # school
        "Form 3",          # form
    ]

    with patch("builtins.input", side_effect=inputs):
        # valid_email and not_empty both call input() internally
        with patch("school.valid_email", return_value="new@email.com"):
            with patch("school.not_empty", side_effect=[
                "Jane Doe", "02-02-2004", "Female", "Zimbabwean",
                "263770000000", "Bulawayo", "Mary Doe",
                "263770000001", "Test High", "Form 3"
            ]):
                add_student({}, str(csv_file))

    content = csv_file.read_text()
    assert "new@email.com" in content
    assert "Jane Doe" in content


def test_add_student_prints_success(tmp_path, capsys):
    """Prints success message after adding."""
    csv_file = tmp_path / "records.csv"
    csv_file.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")

    with patch("school.valid_email", return_value="x@x.com"):
        with patch("school.not_empty", side_effect=[
            "A B", "01-01-2000", "Male", "Zimbabwean",
            "263770000000", "Harare", "Contact", "263770000001",
            "School", "Form 1"
        ]):
            add_student({}, str(csv_file))

    captured = capsys.readouterr()
    assert "successfully" in captured.out.lower()


# ══════════════════════════════════════════════════════════════════════════════
# del_student
# ══════════════════════════════════════════════════════════════════════════════

def test_del_student_removes_from_dict(tmp_path):
    """Email is removed from the dictionary after deletion."""
    csv_file = tmp_path / "records.csv"
    csv_file.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")

    dictionary = dict(SAMPLE)  # copy so SAMPLE isn't mutated

    with patch("builtins.input", return_value="sean@email.com"):
        del_student(dictionary, str(csv_file))

    assert "sean@email.com" not in dictionary


def test_del_student_rewrites_file(tmp_path):
    """Deleted student is absent from the rewritten CSV."""
    csv_file = tmp_path / "records.csv"
    csv_file.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")

    dictionary = dict(SAMPLE)

    with patch("builtins.input", return_value="sean@email.com"):
        del_student(dictionary, str(csv_file))

    content = csv_file.read_text()
    assert "sean@email.com" not in content
    assert "email,full_name" in content  # header still present


def test_del_student_email_not_found(capsys):
    """Prints error and loops when email doesn't exist.
       Second input is a valid email so the loop can exit."""
    dictionary = dict(SAMPLE)

    with patch("builtins.input", side_effect=["wrong@email.com", "sean@email.com"]):
        with patch("builtins.open", mock_open()):  # avoid real file writes
            del_student(dictionary, "dummy.csv")

    captured = capsys.readouterr()
    assert "not found" in captured.out.lower()


pytest.main(["-v", "--tb=line", "-rN", __file__])
