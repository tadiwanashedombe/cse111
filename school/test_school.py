from school import find_record, del_student,add_student,read_csv
import pytest
from unittest.mock import patch

#create a pseudo record
SAMPLE_DATA = {
    "dombe@gmail.com":[
        "dombe@gmail.com" , "Tadiwa Dombe", "25-10-2006", "Male", "Zimbabwean", "263782987606", "54 Rusvingo road, Zengeza 1", "Angela Fungayi", "263782565530", "Alheit High School", "Form 4", "06/17/2026 12:20 PM"
    ]
}


def test_find_record(capsys):
    with patch("builtins.input", return_value = "dombe@gmail.com"):
        result = find_record(SAMPLE_DATA)

    assert result is True

    capture = capsys.readouterr()
    # 1st check
    assert "Tadiwa Dombe" in capture.out
    # 2nd check
    assert "Tadiwa Dombe" in capture.out



   
# test_add_user
def test_add_student(tmp_path):
    records = tmp_path/"records.csv"

    #create create the header
    records.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")

    #record to add
    record = [
       "dombe@gmail.com" , "Tadiwa Dombe", "25-10-2006", "Male", "Zimbabwean", "263782987606", "54 Rusvingo road, Zengeza 1", "Angela Fungayi", "263782565530", "Alheit High School", "Form 4",
    ]

    with patch("builtins.input", side_effect=record):
        # validate email
        with  patch("school.valid_email", return_value = "dombe@gmail.com"):
            #validate empty 
            with patch("school.not_empty", side_effect=[
                "Tadiwa Dombe","25-10-2006", "Male", "Zimbabwean", "263782987606", "54 Rusvingo road, Zengeza 1", "Angela Fungayi", "263782565530", "Alheit High School", "Form 4"
            ]):
                add_student({}, str(records))
        # read the file as a string
        result = records.read_text()

        # 1st check
        assert "dombe@gmail" in result
        # 2nd check
        assert "Tadiwa Dombe" in result

# test_delete_user
def test_del_student(tmp_path):
    # create temp records file
    records = tmp_path/"records.csv"

    #write the header
    records.write_text("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")


    dictionary = dict(SAMPLE_DATA)
    with patch("builtins.input", return_value = "dombe@gmail.com"):
        del_student(dictionary, str(records))

        result = records.read_text()
        #1st check
        assert "dombe@gmail.com" not in result
        
        #2nd check
        assert "Tadiwa Dombe" not in result


pytest.main(["-v", "--tb=line", "-rN", __file__]) 