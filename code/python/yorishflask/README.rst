--------
Build
--------

make sure in folder code/python/yorishflask

.. code::
			
			python -m build



--------------------
Install the Project
--------------------

Use pip to install your project in the virtual environment.

.. code::
			
			$ pip install -e .

OR			

-----------------
Install locally
-----------------

move to root folder code/python

.. code::
            
			python -m pip install ./yorishflask


---------------------------
Initialize database
---------------------------

.. code::
			
			flask --app yorishflask init-db



-----------------------
Running locally
-----------------------

.. code::

			python -m flask --app yorishflask run
