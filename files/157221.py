<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab.4.3"/>
        <attribute name="authors" value="ADVICE"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:39:33 PM"/>
        <attribute name="created" value="QURWSUNFO0RFU0tUT1AtQVFMRklHODsyMDI1LTA3LTE2OzA3OjI5OjEwIFBNOzI3ODk="/>
        <attribute name="edited" value="QURWSUNFO0RFU0tUT1AtQVFMRklHODsyMDI1LTA3LTE2OzA3OjM5OjMzIFBNOzM7MjkwNQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="end"/>
            <while expression="end &gt;= start">
                <output expression="start" newline="True"/>
                <assign variable="start" expression="start+1"/>
            </while>
        </body>
    </function>
</flowgorithm>