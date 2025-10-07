<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work3"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 08:39:01 PM"/>
        <attribute name="created" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0yMDswNzoxMzoxMyBQTTsyNzQx"/>
        <attribute name="edited" value="VXNlcjtMQVBUT1AtMjg4M0RVVU07MjU2OC0wNy0yMDswODozOTowMSBQTTsyOzI4NTY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="start, end, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="start"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <assign variable="i" expression="start"/>
            <while expression="i&lt;=end">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>