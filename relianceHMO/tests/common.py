from faker import Faker

header = {
    "base_url": "",
    "Sandbox-Key": str(Faker().pystr()),
    "Content-Type": "application/json"
}

body = {
    "SignupCompany": {
        "transfer_code": str(Faker().text()),
        "company_name": str(Faker().text()),
        "company_address": str(Faker().text()),
        "state_code": str(Faker().text()),
        "payment_frequency": str(Faker().text()),
        "company_admin": {
            "first_name": str(Faker().text()),
            "last_name": str(Faker().text()),
            "email_address": str(Faker().email()),
            "phone_number": str(Faker().random_int())
        },
        "enrollees": [
            {
                "id": Faker().random_int(),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().email()),
                "phone_number": str(Faker().random_int())

            },
            {
                "id": Faker().random_int(),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().email()),
                "phone_number": str(Faker().random_int())

            }
        ]
    },
    "RenewSubscriptionCompany": {
        "transfer_code": str(Faker().text()),
        "add": [
            {
                "plan_id": Faker().random_int(),
                "firstname": str(Faker().text()),
                "lastname": str(Faker().text()),
                "email": "diana@amazon.com",
                "phone_number": str(Faker().text())
            }
        ],
        "remove": [
            str(Faker().text()),
            str(Faker().text())
        ],
        "update": [
            {
                "plan_id": Faker().random_int(),
                "user_token": str(Faker().text())
            }
        ]
    },
    "RegisterEnrollees": {
        "enrollees": [
            {
                "payment_frequency": str(Faker().text()),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().text()),
                "phone_number": str(Faker().text()),
                "plan_id": str(Faker().text()),
                "can_complete_profile": str(Faker().text()),
                "profile": {
                    "sex": str(Faker().text()),
                    "date_of_birth": str(Faker().text()),
                    "first_name": str(Faker().text()),
                    "last_name": str(Faker().text()),
                    "primary_phone_number": str(Faker().text()),
                    "home_address": str(Faker().text()),
                    "has_smartphone": str(Faker().text()),
                    "profile_picture_filename": str(Faker().text()),
                    "enrollee_type": str(Faker().text()),
                    "hmo_id": str(Faker().text())
                },
                "dependants": [
                    {
                        "first_name": str(Faker().text()),
                        "last_name": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "plan_id": str(Faker().text())
                    }
                ]
            }
        ]
    },
    "SignupIndividuals": {
        "Referral_code": str(Faker().text()),
        "enrollees": [
            {
                "payment_frequency": str(Faker().text()),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().text()),
                "phone_number": str(Faker().text()),
                "plan_id": str(Faker().text()),
                "can_complete_profile": str(Faker().text()),
                "dependants": [
                    {
                        "first_name": str(Faker().text()),
                        "last_name": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "plan_id": str(Faker().text())
                    },
                    {
                        "first_name": str(Faker().text()),
                        "last_name": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "plan_id": str(Faker().text())
                    }
                ]
            },
            {
                "payment_frequency": str(Faker().text()),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().text()),
                "phone_number": str(Faker().text()),
                "plan_id": str(Faker().text()),
                "can_complete_profile": str(Faker().text()),
                "dependants": []
            }
        ]
    },
    "RenewSubscriptionIndividuals": {
        "enrollees": [
            {
                "user_id": str(Faker().text()),
                "remove": [
                    str(Faker().text())
                ]
            }
        ]
    },
    "IndividualSignup": {
        "Referral_code": str(Faker().text()),
        "enrollees": [
            {
                "payment_frequency": str(Faker().text()),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().text()),
                "phone_number": str(Faker().text()),
                "plan_id": str(Faker().text()),
                "can_complete_profile": str(Faker().text()),
                "dependants": [
                    {
                        "first_name": str(Faker().text()),
                        "last_name": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "plan_id": str(Faker().text()),
                    },
                    {
                        "first_name": str(Faker().text()),
                        "last_name": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "plan_id": str(Faker().text()),
                    }
                ]
            },
            {
                "payment_frequency": str(Faker().text()),
                "first_name": str(Faker().text()),
                "last_name": str(Faker().text()),
                "email_address": str(Faker().text()),
                "phone_number": str(Faker().text()),
                "plan_id": str(Faker().text()),
                "can_complete_profile": str(Faker().text()),
                "dependants": []
            }
        ]
    },
    "FundWallet": {
        "amount": str(Faker().text())
    }
}

params = {
    "RequestConsultation": {
        "patient_id": str(Faker().text()),
        "reason": str(Faker().text())
    },
    "GetAllEnrollee": {
        "page": str(Faker().text()),
        "limit": str(Faker().text())
    },
    "GetEnrollee":  {
        "hmo_id": str(Faker().text())
    },
    "CompleteEnrolleeProfile": {
        "sex": str(Faker().text()),
        "date_of_birth": str(Faker().text()),
        "home_address": str(Faker().text()),
        "has_smartphone": str(Faker().text()),
        "profile_picture_filename": str(Faker().text()),
        "hash": str(Faker().text())
    },
    "EnrolleesValidation": {
        "hmo_id": str(Faker().text())
    },
    "EnrolleesIDCard": {
        "hmo_id": str(Faker().text())
    },
    "GetAllPlans": {
        "type": str(Faker().text()),
        "package": str(Faker().text())
    },
    "GetHealthcareProviders": {
        "state": str(Faker().text()),
        "plan_id": str(Faker().text()),
        "tiers": str(Faker().text()),
        "page": str(Faker().text()),
        "limit": str(Faker().text())
    },
    "BenefitsList": {
        "plan": str(Faker().text())
    }
}

responses = {
    "SignupCompany": {
        "message": str(Faker().text()),
        "data": {
            "status": str(Faker().text()),
            "data": [
                {
                    "id": Faker().random_int(),
                    "hmo_id": str(Faker().text()),
                    "profile_hash": str(Faker().text()),
                    "first_name": str(Faker().text()),
                    "last_name": str(Faker().text()),
                    "phone_number": str(Faker().random_int()),
                    "email_address": str(Faker().email()),
                    "plan_name": str(Faker().text()),
                    "type": str(Faker().text()),
                    "status": str(Faker().text()),
                    "cover_start_date": str(Faker().date()),
                    "cover_end_date": str(Faker().date()),
                    "dependants": [
                        {
                            "id": Faker().random_int(),
                            "hmo_id": str(Faker().text()),
                            "first_name": str(Faker().text()),
                            "last_name": str(Faker().text()),
                            "phone_number": str(Faker().random_int()),
                            "email_address": str(Faker().email()),
                            "plan_name": str(Faker().text()),
                            "type": str(Faker().text()),
                            "status": str(Faker().text()),

                        }
                    ]
                },
                {
                    "id": Faker().random_int(),
                    "hmo_id": str(Faker().text()),
                    "first_name": str(Faker().text()),
                    "last_name": str(Faker().text()),
                    "phone_number": str(Faker().random_int()),
                    "email_address": str(Faker().email()),
                    "plan_name": str(Faker().text()),
                    "type": str(Faker().text()),
                    "status": str(Faker().text()),
                    "dependants": []
                }
            ],
            "meta": {
                "pages": Faker().random_int(),
                "current_page": Faker().random_int(),
                "per_page": Faker().random_int(),
                "total": Faker().random_int()
            }
        }
    },
    "RenewSubscriptionCompany": {
        "message": str(Faker().text()),
        "data": {
            "status": str(Faker().text()),
            "data": {
                "invoice_code": str(Faker().text()),
                "transfer_code": str(Faker().text()),
                "total_price": Faker().random_int(),
                "expires_at": str(Faker().date()),
                "added": [
                    {
                        "firstname": str(Faker().text()),
                        "lastname": str(Faker().text()),
                        "email": str(Faker().email()),
                        "phone_number": str(Faker().text()),
                        "user_token": str(Faker().text())
                    }
                ],
                "removed": [
                    str(Faker().text()),
                    str(Faker().text())
                ],
                "updated": [
                    {
                        "plan_id": Faker().random_int(),
                        "user_token": str(Faker().text())
                    }
                ]
            }
        }
    },
    "RegisterEnrollees": {
        "message": str(Faker().text()),
        "data": {
            "status": str(Faker().text()),
            "data": {
                "transfer_code": str(Faker().text()),
                "enrollees": {
                    "successful": [
                        {
                            "email_address": str(Faker().text()),
                            "phone_number": str(Faker().text()),
                            "user_id": str(Faker().text()),
                            "plan_id": str(Faker().text()),
                            "payment_frequency": str(Faker().text()),
                            "hash": str(Faker().text()),
                            "dependants": [
                                {
                                    "email_address": str(Faker().text()),
                                    "phone_number": str(Faker().text()),
                                    "user_id": str(Faker().text()),
                                    "hash": str(Faker().text()),
                                    "plan_id": str(Faker().text())
                                },
                                {
                                    "email_address": str(Faker().text()),
                                    "phone_number": str(Faker().text()),
                                    "user_id": str(Faker().text()),
                                    "hash": str(Faker().text()),
                                    "plan_id": str(Faker().text())
                                }
                            ],
                            "expires_at": str(Faker().text())
                        }
                    ],
                    "failed": [
                        {
                            "invoice_code": str(Faker().text()),
                            "message": str(Faker().text()),
                            "email_address": str(Faker().text()),
                            "phone_number": str(Faker().text()),
                            "dependants": []
                        }
                    ]
                }
            }
        }
    },
    "GetAllEnrollee": {
        "message": str(Faker().text()),
        "data": {
            "status": str(Faker().text()),
            "data": [
                {
                    "id": str(Faker().text()),
                    "hmo_id": str(Faker().text()),
                    "profile_hash": str(Faker().text()),
                    "first_name": str(Faker().text()),
                    "last_name": str(Faker().text()),
                    "phone_number": str(Faker().text()),
                    "email_address": str(Faker().text()),
                    "plan_name": str(Faker().text()),
                    "type": str(Faker().text()),
                    "status": str(Faker().text()),
                    "cover_start_date": str(Faker().text()),
                    "cover_end_date": str(Faker().text()),
                    "dependants": [
                        {
                            "id": str(Faker().text()),
                            "hmo_id": str(Faker().text()),
                            "first_name": str(Faker().text()),
                            "last_name": str(Faker().text()),
                            "phone_number": str(Faker().text()),
                            "email_address": str(Faker().text()),
                            "plan_name": str(Faker().text()),
                            "type": str(Faker().text()),
                            "status": str(Faker().text())
                        }
                    ]
                },
                {
                    "id": str(Faker().text()),
                    "hmo_id": str(Faker().text()),
                    "first_name": str(Faker().text()),
                    "last_name": str(Faker().text()),
                    "phone_number": str(Faker().text()),
                    "email_address": str(Faker().text()),
                    "plan_name": str(Faker().text()),
                    "type": str(Faker().text()),
                    "status": str(Faker().text()),
                    "dependants": []
                }
            ],
            "meta": {
                "pages": str(Faker().text()),
                "current_page": str(Faker().text()),
                "per_page": str(Faker().text()),
                "total": str(Faker().text())
            }
        }
    },
    "RequestConsultation": {
        "status": str(Faker().text()),
        "data": {
            "consultation_id": str(Faker().text()),
            "created_at": str(Faker().text())
        }
    },
    "GetEnrollee":  {
        "status": str(Faker().text()),
        "data": {
            "id": str(Faker().text()),
            "hmo_id": str(Faker().text()),
            "first_name": str(Faker().text()),
            "last_name": str(Faker().text()),
            "phone_number": str(Faker().text()),
            "email_address": str(Faker().text()),
            "plan_name": str(Faker().text()),
            "cover_start_date": str(Faker().text()),
            "cover_end_date": str(Faker().text()),
            "type": str(Faker().text()),
            "status": str(Faker().text()),
            "dependants": []
        }
    },
    "CompleteEnrolleeProfile":  {
        "status": str(Faker().text()),
        "data": {
            "message": str(Faker().text()),
            "hmo_id": str(Faker().text())
        }
    },
    "EnrolleesValidation": {
        "status": str(Faker().text()),
        "data": {
            "first_name": str(Faker().text()),
            "last_name": str(Faker().text()),
            "email_address": str(Faker().text()),
            "phone_number": str(Faker().text()),
            "plan": {
                "name": str(Faker().text()),
                "cover_start_date": str(Faker().text()),
                "cover_end_date": str(Faker().text()),
                "amount": str(Faker().text())
            }
        }
    },
    "EnrolleesIDCard": {
        "status": str(Faker().text()),
        "data": {
            "id": 563,
            "hmo_id": str(Faker().text()),
            "first_name": str(Faker().text()),
            "last_name": str(Faker().text()),
            "phone_number": str(Faker().text()),
            "email_address": str(Faker().text()),
            "plan_name": str(Faker().text()),
            "cover_start_date": str(Faker().text()),
            "cover_end_date": str(Faker().text()),
            "type": str(Faker().text()),
            "status": str(Faker().text()),
            "dependants": []
        }
    },
    "GetAllPlans": {
        "status": str(Faker().text()),
        "data": {
            "plans": [
                {
                    "id": 25,
                    "class": 12,
                    "type": str(Faker().text()),
                    "name": str(Faker().text()),
                    "no_of_dependants": str(Faker().text()),
                    "has_pec": str(Faker().text()),
                    "provider_tiers": str(Faker().text()),
                    "summary": [
                        {
                            "name": str(Faker().text()),
                            "value": str(Faker().text()),
                        },
                        {
                            "name": str(Faker().text()),
                            "value": str(Faker().text()),
                        },
                        {
                            "name": str(Faker().text()),
                            "value": str(Faker().text()),
                        }
                    ],
                    "price": {
                        "monthly": str(Faker().text()),
                        "quarterly": str(Faker().text()),
                        "yearly": str(Faker().text()),
                    }
                }
            ]
        }
    },
    "IndividualSignup": {
        "status": str(Faker().text()),
        "data": {
            "transfer_code": str(Faker().text()),
            "enrollees": {
                "successful": [
                    {
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "user_id": str(Faker().text()),
                        "plan_id": str(Faker().text()),
                        "payment_frequency": str(Faker().text()),
                        "hash": str(Faker().text()),
                        "dependants": [
                            {
                                "email_address": str(Faker().text()),
                                "phone_number": str(Faker().text()),
                                "user_id": str(Faker().text()),
                                "hash": str(Faker().text()),
                                "plan_id": str(Faker().text()),
                            },
                            {
                                "email_address": str(Faker().text()),
                                "phone_number": str(Faker().text()),
                                "user_id": str(Faker().text()),
                                "hash": str(Faker().text()),
                                "plan_id": str(Faker().text()),
                            }
                        ],
                        "expires_at": str(Faker().text()),
                    }
                ],
                "failed": [
                    {
                        "invoice_code": str(Faker().text()),
                        "message": str(Faker().text()),
                        "email_address": str(Faker().text()),
                        "phone_number": str(Faker().text()),
                        "dependants": [],
                    }
                ]
            }
        }
    },
    "RenewSubscriptionIndividuals": {
        "status": str(Faker().text()),
        "data": {
            "transfer_code": str(Faker().text()),
            "enrollees": {
                "successful": [
                    {
                        "email_address": str(Faker().text()),
                        "user_id": str(Faker().text()),
                        "expires_at": str(Faker().text()),
                        "dependants": [
                            {
                                "email_address": str(Faker().text()),
                                "phone_number": str(Faker().text()),
                                "user_id": str(Faker().text()),
                                "plan_id": str(Faker().text()),
                            }
                        ]
                    }
                ],
                "failed": []
            }
        }
    },
    "GetHealthcareProviders":  {
        "status": str(Faker().text()),
        "data": [
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
                "location": str(Faker().text()),
                "address": str(Faker().text()),
                "tier": str(Faker().text())
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
                "location": str(Faker().text()),
                "address": str(Faker().text()),
                "tier": str(Faker().text())
            }
        ],
        "pagination": {
            "current_page": str(Faker().text()),
            "last_page": str(Faker().text()),
            "per_page": str(Faker().text()),
            "total": str(Faker().text()),
            "count": str(Faker().text())
        }
    },
    "GetStatesAvailable":  {
        "status": str(Faker().text()),
        "data": [
            {
                "code": str(Faker().text()),
                "name": str(Faker().text())
            }
        ]
    },
    "BenefitsList": {
        "status": str(Faker().text()),
        "data": [
            {
                "name": str(Faker().text()),
                "details": [
                    {
                        "plan": str(Faker().text()),
                        "value": str(Faker().text()),
                        "group": str(Faker().text()),
                        "quarter": str(Faker().text())
                    },
                    {
                        "plan": str(Faker().text()),
                        "value": str(Faker().text()),
                        "group": str(Faker().text()),
                        "quarter": str(Faker().text())
                    }
                ]
            }
        ]
    },
    "GetTitles": {
        "status":  str(Faker().text()),
        "data": [
            {
                "id": str(Faker().text()),
                "name":  str(Faker().text()),
                "abbreviation":  str(Faker().text())
            },
            {
                "id":  str(Faker().text()),
                "name":  str(Faker().text()),
                "abbreviation":  str(Faker().text())
            },
            {
                "id":  str(Faker().text()),
                "name":  str(Faker().text()),
                "abbreviation":  str(Faker().text())
            }
        ]
    },
    "GetOccupations": {
        "status": str(Faker().text()),
        "data": [
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            }
        ]
    },
    "GetMaritalStatus": {
        "status": str(Faker().text()),
        "data": [
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            },
            {
                "id": str(Faker().text()),
                "name": str(Faker().text()),
            }
        ]
    },
    "WalletBalance":  {
        "status": str(Faker().text()),
        "data": [
            {
                "balance": str(Faker().text())
            }
        ]
    },
    "FundWallet": {
        "status": str(Faker().text()),
        "data": {
            "payment_url": str(Faker().text()),
            "amount": str(Faker().text())
        }
    },
    "PartnershipWalletTransactions": {
        "status": str(Faker().text()),
        "data": [
            {
                "id": str(Faker().text()),
                "user_id": str(Faker().text()),
                "amount": str(Faker().text()),
                "wallet_balance": str(Faker().text()),
                "wallet_transaction_type_id": str(Faker().text()),
                "payment_id": str(Faker().text()),
                "payment_state_id": str(Faker().text()),
                "transaction_reference": str(Faker().text()),
                "transfer_code": str(Faker().text()),
                "created_at": str(Faker().text()),
                "active_status": str(Faker().text())
            },
            {
                "id": str(Faker().text()),
                "user_id": str(Faker().text()),
                "amount": str(Faker().text()),
                "wallet_balance": str(Faker().text()),
                "wallet_transaction_type_id": str(Faker().text()),
                "payment_id": str(Faker().text()),
                "payment_state_id": str(Faker().text()),
                "transaction_reference": str(Faker().text()),
                "transfer_code": str(Faker().text()),
                "created_at": str(Faker().text()),
                "active_status": str(Faker().text())
            }
        ],
        "pagination": {
            "current_page": str(Faker().text()),
            "last_page": str(Faker().text()),
            "per_page": str(Faker().text()),
            "total": str(Faker().text()),
            "count": str(Faker().text())
        }
    }
}


class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text

    def json(self):
        return self.text
