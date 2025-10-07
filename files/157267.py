<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 08:33:57 AM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtUlFSMlJOTDY7MjU2OC0wNy0xNzswODoxMjoyMSBBTTsyNzg4"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtUlFSMlJOTDY7MjU2OC0wNy0xNzswODozMzo1NyBBTTsyOzI5MDk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num1, num2, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="num1"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="num2"/>
            <output expression="num1" newline="True"/>
            <while expression="num1 &lt; num2">
                <assign variable="num1" expression="num1 + 1"/>
                <output expression="num1" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>