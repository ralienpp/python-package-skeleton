Overview
--------

This is a Python package skeleton that demonstrates what directory layout to use and which files are necessary.


Installation
------------

``pip install git+https://github.com/ralienpp/python-package-skeleton.git``



Example
-------
::

    from acmepack.core import Nucleus
    n = Nucleus()
    print n.test(3)
    
    
    
Architecture
------------

This diagram is here just to give you an example of how handy it is to have the documentation at your fingertips. The diagram itself is not related to this project, it was generated with PlantUML::

         ┌─────────────────┐          ┌────────────┐          ┌────┐                     ┌──────┐     
         │bkts_card_monitor│          │t_smart_card│          │bkts│                     │Server│     
         └────────┬────────┘          └─────┬──────┘          └─┬──┘                     └──┬───┘     
                  │                         │                   │                           │         
                  │                         ╔════════════════╗  │                           │         
    ══════════════╪═════════════════════════╣ Card insertion ╠══╪═══════════════════════════╪═════════
                  │                         ╚════════════════╝  │                           │         
                  │                         │                   │                           │         
                  │   POST `[card ID] 1`    │                   │                           │         
                  │────────────────────────>│                   │                           │         
                  │                         │                   │                           │         
                  │                         │   `[card ID] 1`   │                           │         
                  │                         │ ──────────────────>                           │         
                  │                         │                   │                           │         
                  │                         │                   │ POST q_bkts_smart_cards   │         
                  │                         │                   │ H:card_id=[id],state:True │         
                  │                         │                   │ ──────────────────────────>         
                  │                         │                   │                           │         
                  │                         │                   │                           │         
                  │                         │╔══════════════╗   │                           │         
    ══════════════╪═════════════════════════╪╣ Card removal ╠═══╪═══════════════════════════╪═════════
                  │                         │╚══════════════╝   │                           │         
                  │                         │                   │                           │         
                  │   POST `[card ID] 0`    │                   │                           │         
                  │────────────────────────>│                   │                           │         
                  │                         │                   │                           │         
                  │                         │   `[card ID] 0`   │                           │         
                  │                         │ ──────────────────>                           │         
                  │                         │                   │                           │         
                  │                         │                   │ POST q_bkts_smart_cards   │         
                  │                         │                   │ H:card_id=[id],state:False│         
                  │                         │                   │ ──────────────────────────>         
         ┌────────┴────────┐          ┌─────┴──────┐          ┌─┴──┐                     ┌──┴───┐     
         │bkts_card_monitor│          │t_smart_card│          │bkts│                     │Server│     
         └─────────────────┘          └────────────┘          └────┘                     └──────┘     
         
         
         
         
This is not related to the project either, but it is nice to see what components the project is made of; this fantastic drawing was made with ASCIIflow::


                                            +-----------+
                                            |           |
                                            | SERVER    |            pub/sub
                                            |           <----------------------------+
                                            |           |                            |
                                            |           |                            |
                                            +-----------+                            |
                                                                                     |
                                           +------------+                            |
      +--------------+       pub           | MQTT broker|                    +-------+----------+
      | Validator 1  +----------+          |            |                    |       bkts       |
      |              |          |        t_last_will <------.   subscribe    |      worker      |
      +--------------+          +------+>t_requests <------------------------+                  |
                                       |   |            |                    +------+----+------+
                                       |   |            |               pub         |    |
      +--------------+                 |   |          /validator_1 <----------------+    |
      | Validator N  |       pub       |   |            |                                |
      |              +-----------------+   |            |   ...                          |
      +-----------+--+                     |            |                                |
                  |                        |            |                pub             |
                  |                        |          /validator_N <---------------------+
                  |                        |            |    ^
                  |                        +------------+    |
                  |                                          |
                  |            subscribe                     |
                  +------------------------------------------+
