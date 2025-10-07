<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_03"/>
        <attribute name="authors" value="Staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 01:16:25 PM"/>
        <attribute name="created" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMjA7MDE6MDE6MjQgUE07Mjg4NA=="/>
        <attribute name="edited" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMjA7MDE6MTY6MjUgUE07MjszMDAw"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numStart" type="Integer" array="False" size=""/>
            <declare name="numEnd" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="numStart"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="numEnd"/>
            <while expression="numStart &lt;= numEnd">
                <output expression="numStart" newline="True"/>
                <assign variable="numStart" expression="numStart + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>