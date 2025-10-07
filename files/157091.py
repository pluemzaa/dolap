<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Tannn"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:44:45 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6MDk6MDggUE07MjU4MQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6NDQ6NDUgUE07NDsyNjkz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="snumber, ennumber" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="snumber"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="ennumber"/>
            <while expression="snumber &lt;= ennumber">
                <output expression="snumber" newline="True"/>
                <assign variable="snumber" expression="snumber + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>