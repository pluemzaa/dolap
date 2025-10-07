<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_3"/>
        <attribute name="authors" value="MY PC JO E"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 05:11:24 PM"/>
        <attribute name="created" value="TVkgUEMgSk8gRTtTTFVQUElFWEJBUlpFRDsyNTY4LTA3LTE5OzA0OjU2OjU0IFBNOzMwMTE="/>
        <attribute name="edited" value="TVkgUEMgSk8gRTtTTFVQUElFWEJBUlpFRDsyNTY4LTA3LTE5OzA1OjExOjI0IFBNOzE7MzEwOA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="count, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <assign variable="count" expression="0"/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="count"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="i"/>
            <while expression="count&lt;=i">
                <output expression="count" newline="True"/>
                <assign variable="count" expression="count+1"/>
            </while>
        </body>
    </function>
</flowgorithm>