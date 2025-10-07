<?xml version="1.0"?>
<flowgorithm fileversion="3.0">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="bamboo"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 08:48:14 "/>
        <attribute name="created" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMDg6NDE6NDYgIjsyNzcw"/>
        <attribute name="edited" value="YmFtYm9vO01BQ0JPT0tBSVJCQU07MjU2OC0wNy0yMjsiMDg6NDg6MTQgIjsxOzI4ODA="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="numStart" type="Integer" array="False" size=""/>
            <declare name="numEnd" type="Integer" array="False" size=""/>
            <output expression="&quot; Input start number:&quot;" newline="True"/>
            <input variable="numStart"/>
            <output expression="&quot; Input end number: &quot;" newline="True"/>
            <input variable="numEnd"/>
            <while expression="numStart &lt;= numEnd">
                <output expression="numStart" newline="True"/>
                <assign variable="numstart" expression="numStart + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>