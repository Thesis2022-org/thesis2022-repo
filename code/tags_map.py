


def tag_Ahohfeld(self):
    TAG_Aholfed = {}
    TAG_Aholfed ["RIGHT"] = "<b>RIGHT(person_1;person_2;action_s)</b><br /> \
                        person_1 has a RIGHT that person_2 do action_s, means,<br /> \
                        person_2 has a DUTY to person_1 to do action_s,which in turn means,<br />\
                        IT IS OBLIGATORY THAT action_s be done by person_2 for person_2,which,<br />\
                        in turn means operationally in terms of how the legal system will treat the matter,<br />\
                        IF      1. IT IS NOT SO THAT person_2 does action_s for person_1,<br />\
                        THEN    2. person_2 has violated her DUTY to person_1, AND,<br />\
                                3. IF person_1 seeks remedy in the legal system by litigating, <br />\
                                THEN the legal system will provide a remedy to person_1 with respect to person_2"

    TAG_Aholfed ["DUTY"] = "<b>DUTY(person_1;person_2;action_s)</b><br />\
                            person_1 has a DUTY to person_2 to do action_s, means<br /> \
                            IT IS OBLIGATORY_THAT action_s be done by person_1 for person_2, <br />\
                            which in turn means operationally in terms of how the legal system will treat the matter <br />\
                            IF  1. IT IS NOT SO THAT person_1 does action_s for person_2,THEN <br />\
                            2. person_1 has violated her DUTY to person_b, AND <br />\
                            3. IF person_2 seeks remedy in the legal system by litigating, <br />\
                            THEN the legal system will provide a remedy to person_1 with respect to person"

    TAG_Aholfed["NO_RIGHT"] = "<b>NO_RIGHT(person_1;person_2;action_s)</b><br /> \
                            person_1 has a NO_RIGHT that person_2 do action_s, means<br /> \
                            IT IS NOT SO THAT person_2 has a DUTY to person_1 to do action_s, which in turn means<br /> \
                            IT IS NOT SO THAT IT IS OBLIGATORY THAT action_s be done by person_2 for person_1,  <br /> \
                            which in turn means operationally in terms of how the legal system will treat the matter<br /> \
                            IF 1. person_2 does action_s with respect to person_1,<br /> \
                            THEN 2. person_2 has NOT violated any DUTY to person_1, AND<br /> \
                            3. IF person_1 seeks remedy in the legal system by litigating,<br />  \
                            THEN the legal system will NOT provide a remedy to person_1 with respect to person_2."

    TAG_Aholfed["PRIVILEGE"]= "<b>PRIVILEGE(person_1,person_2,action_s)</b><br /> \
                            person_1 has a PRIVILEGE with respect to person_2 to do action means<br /> \
                            IT IS NOT SO THAT person_1 has a DUTY to person_2 to do NEG action_s,which in turn means<br /> \
                            IT IS NOT SO THAT IT IS OBLIGATORY THAT NEG action_s be done by person_1 for person_2,<br /> \
                            which in turn means operationally in terms of how the legal system will treat the matter<br /> \
                            IF  1. person_1 does action_s with respect to person_2,<br /> \
                            THEN 2. IT IS NOT SO THAT person_1 has violated a DUTY to person_2,AND <br /> \
                            3. IF person_2 seeks remedy in the legal system by litigating, THEN <br /> \
                            IT IS NOT SO THAT the legal system will provide a remedy to person_2 with respect to person_1"

    TAG_Aholfed["COND_PRIVILEGE"]="<b>COND_PRIVILEGE(person_1;person_2;action_s;event_e;condition_c)</b><br />\
                                person_1 has a COND_PRIVILEGE with respect to person_2 to do action_s means<br />\
                                person_2 has a COND_NO_RIGHT that person_1 do NEG action_s. which, in turn, means<br />\
                                person_2 has a RIGHT that pl do NEG action_s, AND there is an event_e such that<br />\
                                1. it is naturally possible for event_e to occur, AND<br />\
                                2. IF event_e occurs, THEN condition_c is fulfilled, AND<br />\
                                3. IF condition_c is fulfilled, THEN person_2 NO_RIGHT that person_1 do NEG action_s is created<br /> \
                                (which is another way of saying that person_2 RIGHT that person_1 do NEG action_s is terminated,<br /> \
                                which in turn is another way of saying that person_1 PRIVILEGE with respect to person_2 to do action_s is created)"

    TAG_Aholfed["COND_DUTY"] = "<b>COND_DUTY(person_1;person_2;action_s;event_e;condition_c)</b><br />\
                                person_1 has a PRIVILEGE with respect to person_2 to do NEG action_s AND there is an event_e such that,<br /> \
                                1. it is naturally possible for event_e to occur, AND <br />\
                                2. IF event_e occurs, THEN condition_c is fulfilled, AND <br />\
                                3. IF condition_c is fulfilled, THEN person_1 DUTY to person_2 do action_s is created<br />\
                                (which is another way of saying that person_1 PRIVILEGE with respect to person_2 to do NEG action_s is terminated)"

    TAG_Aholfed["COND_NOT_RIGHT"] = "<b>COND_NOT_RIGHT(person_1;person_2;action_s;event_e;condition_c)</b><br />\
                                    person_1 has a PRIVILEGE with respect to person_2 to do NEG action_s AND there is an event_e such that,<br /> \
                                    1. it is naturally possible for event_e to occur, AND <br />\
                                    2. IF event_e occurs, THEN condition_c is fulfilled, AND <br />\
                                    3. IF condition_c is fulfilled, THEN person_1 DUTY to person_2 do action_s is created<br />\
                                    (which is another way of saying that person_1 PRIVILEGE with respect to person_2 to do NEG action_s is terminated)"

    TAG_Aholfed["COND_RIGHT"] = "<b>COND_RIGHT(person_1;person_2;action_s;event_e;condition_c)</b><br />\
                                    person_1 has a PRIVILEGE with respect to person_2 to do NEG action_s AND there is an event_e such that,<br /> \
                                    1. it is naturally possible for event_e to occur, AND <br />\
                                    2. IF event_e occurs, THEN condition_c is fulfilled, AND <br />\
                                    3. IF condition_c is fulfilled, THEN person_1 DUTY to person_2 do action_s is created<br />\
                                    (which is another way of saying that person_1 PRIVILEGE with respect to person_2 to do NEG action_s is terminated)"
    TAG_Aholfed["FORBIDDEN_THAT"] = "<b>FORBIDDEN_THAT(action_s)</b><br />\
                                     IF 1. the state of affairs described by action_s is so,THEN<br />\
                                        2. there is a violation, AND <br />\
                                        3. the legal system will provide a remedy with respect to the violator"

    return TAG_Aholfed
