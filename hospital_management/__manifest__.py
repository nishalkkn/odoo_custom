{
    'name':"Hospital management",
    'application':True,

    'data':[
        'views/hospital_management.xml',
        'views/hospital_patient.xml',
        'views/hospital_op_ticket.xml',
        'views/hospital_doctor.xml',
        'security/ir.model.access.csv',
        'views/hospital_department.xml',
        'views/hospital_consultation.xml',
        'data/my_module_sequence.xml',
    ],

    'depends' : ['contacts','hr'],
    'license': 'LGPL-3',

}